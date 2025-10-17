from event_to_string import event_to_string

class StateMachine:
    def __init__(self, start_state, state_transitions):
        self.cur_state = start_state
        self.state_transitions = state_transitions
        # 시작 상태의 enter 호출 (이벤트가 필요하면 None 전달)
        self.cur_state.enter(None)

    def update(self):
        self.cur_state.do()

    def handle_event(self, event):
        transitions = self.state_transitions.get(self.cur_state, {})
                    # 상태 전환
                    self.cur_state.exit(event)
                    next_state = transitions[check_event]
                    next_state.enter(event)
                    print(f'{self.cur_state.__class__.__name__} - {event_to_string(event)} -> {next_state.__class__.__name__}')
                    self.cur_state = next_state
#처리되지 않은 이벤트를 출력
        # 처리되지 않은 이벤트를 출력

    def draw(self):
        self.cur_state.draw()

