#pragma once
#include <stdio.h>
#include <stdlib.h>

inline void error ( char *message ) {
	printf("%s\n", message);
	exit(1);
}

const int MAX_STACK_SIZE = 20;

class CArrayStack
{
	int	m_top;			// 요소의 개수
	int	m_data[MAX_STACK_SIZE];	// 요소의 배열

public:

	CArrayStack(void)	{ m_top = -1; }
	~CArrayStack(void)	{ 	}

	void Reset()	{ m_top = -1; }
	bool IsEmpty()	{ return m_top == -1; }
	bool IsFull()	{ return m_top == MAX_STACK_SIZE; }

	void Push ( int e ) {	// 맨 위에 항목 삽입
		if( IsFull() ) {
			error("Error: 스택 포화 에러\n");
			return;
		}
		m_data[++m_top] = e;
	}

	int Pop ( ) {		// 맨 위의 요소를 삭제하고 반환
		if( IsEmpty() ) 
			error("Error: 스택 공백 에러 Pop()\n");
		return m_data[m_top--];
	}

	int Peek ( ){		// 삭제하지 않고 요소 반환
		if( IsEmpty() ) 
			printf("Error: 스택 공백 에러 Peek()\n");
		return m_data[m_top];
	}

	// 추가적인 멤버 함수
	void Display ( ) {		// 스택 내용을 화면에 출력
		printf("[스택 항목의 수 = %2d] ==> ", m_top+1) ;
		for (int i=0 ; i<=m_top ; i++ )
			printf("%c ", m_data[i]);
		printf("\n");
	}

};

