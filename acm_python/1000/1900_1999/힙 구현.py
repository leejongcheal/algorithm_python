class Heap:
    # 개체들이 공유하는 메소드는 클래스 메소드로 만들어도 된다.
    def get_parent_idx(self, idx):
        return idx // 2

    def get_left_child_idx(self, idx):
        return idx * 2

    def get_right_child_idx(self, idx):
        return idx * 2 + 1

    # 중요함수- 보통은 유저 프로그래머가 직접 구현, 인터페이스만 제공
    # 우선순위에 따라 반환값이 달라진다.
    def get_prior(self, value1, value2):
        '''
        value1 이 우선순위가 높으면 -1 리턴
        value2 가 우선순위가 높으면 1 리턴
        두 우선순위가 같다면 0을 리턴
        '''
        # min_max == 1 ==> 최소 힙
        if self.min_max == 1:
            if value1 < value2:
                return -1
            elif value1 > value2:
                return 1
            else:
                return 0
        else:  # self.min_max == 2 ==> 최대 힙
            if value1 > value2:
                return -1
            elif value1 < value2:
                return 1
            else:
                return 0

    def __init__(self, s_min_max='min'):
        self.dynamic_arr = [
            None, ]  # one based index, 다른 언어는 가변배열을 사용한다. C++은 백터 사용, 효율 좋게 짜는 것이 중요(가변배열이 수정시마다 매번 탐색, 복사,
        # 삭제를 하면 메모리 낭비)
        self.num_of_data = 0  # 마지막 데이터의 index

        if s_min_max == 'max':
            self.min_max = 2
        else:
            self.min_max = 1

    def is_empty(self):
        if self.num_of_data == 0:
            return True

        return False

    def size(self):  # ADT에 없는 함수이지만 테스트용으로 만듬
        return self.num_of_data

    # insert 메서드에서 사용
    # 부모 값과 비교해서, 우선순위가 부모 보다 높으면 True 낮으면 False
    def is_go_up(self, idx, data):
        if idx <= 1:
            return False
        parent_value = self.dynamic_arr[self.get_parent_idx(idx)]
        if self.get_prior(parent_value, data) == 1:  # 부모 우선순위가 작다면
            return True
        else:
            return False

    def insert(self, data):
        if self.is_empty():
            self.dynamic_arr.append(data)
            self.num_of_data += 1
            return

        self.dynamic_arr.append(data)
        self.num_of_data += 1

        idx_data = self.num_of_data

        while self.is_go_up(idx_data, data):
            parent_idx = self.get_parent_idx(idx_data)
            self.dynamic_arr[idx_data] = self.dynamic_arr[parent_idx]
            idx_data = parent_idx

        self.dynamic_arr[idx_data] = data

    # 우선순위가 높은 자식 노드의 인덱스를 반환
    def which_is_prior_child(self, idx):
        left_idx = self.get_left_child_idx(idx)

        if left_idx > self.num_of_data:
            return None
        elif left_idx == self.num_of_data:
            return left_idx

        right_idx = self.get_right_child_idx(idx)

        left_value = self.dynamic_arr[left_idx]
        right_value = self.dynamic_arr[right_idx]

        if self.get_prior(left_value, right_value) == -1:
            return left_idx
        else:
            return right_idx

    def is_go_down(self, idx, data):
        child_idx = self.which_is_prior_child(idx)

        if not child_idx:
            return False

        child_value = self.dynamic_arr[child_idx]

        if self.get_prior(child_value, data) == -1:
            return True
        else:
            return False

    def delete(self):
        if self.is_empty():
            return None

        ret_data = self.dynamic_arr[1]
        last_data = self.dynamic_arr[self.num_of_data]
        self.num_of_data -= 1

        idx_data = 1

        while self.is_go_down(idx_data, last_data):
            child_idx = self.which_is_prior_child(idx_data)
            self.dynamic_arr[idx_data] = self.dynamic_arr[child_idx]
            idx_data = child_idx

        self.dynamic_arr[idx_data] = last_data
        self.dynamic_arr.pop()

        return ret_data


if __name__ == "__main__":
    heap = Heap("min")
    heap.insert(3)
    heap.insert(5)
    heap.insert(1)
    heap.insert(10)
    heap.insert(8)
    heap.insert(7)
    heap.insert(4)
    heap.insert(5)
    heap.insert(2)
    heap.insert(6)
    heap.insert(9)

    for i in range(1, heap.size() + 1):
        print(heap.dynamic_arr[i], end='  ')
        # 1  2  3  5  6  7  4  10  5  8  9

    print("\n")

    for i in range(1, heap.size() + 2):
        print(heap.delete(), end='  ')
        # 1  2  3  4  5  5  6  7  8  9  10
