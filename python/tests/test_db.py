#  Copyright 2023 LanceDB Developers
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import lancedb


def test_basic(tmp_path):
    db = lancedb.connect(tmp_path)
    table = db.create_table("test",
                            data=[{"vector": [3.1, 4.1], "item": "foo", "price": 10.0},
                                  {"vector": [5.9, 26.5], "item": "bar", "price": 20.0}])
    rs = table.search([100, 100]).limit(1).to_df()
    assert len(rs) == 1
    assert rs["item"].iloc[0] == "bar"

    rs = table.search([100, 100]).where("price < 15").limit(1).to_df()
    assert len(rs) == 1
    assert rs["item"].iloc[0] == "foo"