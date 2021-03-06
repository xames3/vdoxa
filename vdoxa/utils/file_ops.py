# Copyright 2020 XAMES3. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ======================================================================
"""Utility for simplifying file operations."""

import os


def get_file_name(path: str) -> str:
    """Return filename."""
    name = (os.path.basename(path).split('.')[0]).lower()
    if len(name) > 10:
        return name[:11]
    else:
        return name


def get_directory_name(path: str) -> str:
  """Get directory where the videos will be stored."""
  return os.path.join(os.path.dirname(path), get_file_name(path))


def create_directory(path: str) -> None:
    """Create directory with file name"""
    if not os.path.isdir(get_directory_name(path)):
      os.mkdir(get_directory_name(path))


def filename(path:str, video_number: int) -> str:
  create_directory(path)
  return os.path.join(get_directory_name(path),
                      f'{get_file_name(path)}_{video_number}.mp4')
