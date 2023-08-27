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
	int	m_top;			// ����� ����
	int	m_data[MAX_STACK_SIZE];	// ����� �迭

public:

	CArrayStack(void)	{ m_top = -1; }
	~CArrayStack(void)	{ 	}

	void Reset()	{ m_top = -1; }
	bool IsEmpty()	{ return m_top == -1; }
	bool IsFull()	{ return m_top == MAX_STACK_SIZE; }

	void Push ( int e ) {	// �� ���� �׸� ����
		if( IsFull() ) {
			error("Error: ���� ��ȭ ����\n");
			return;
		}
		m_data[++m_top] = e;
	}

	int Pop ( ) {		// �� ���� ��Ҹ� �����ϰ� ��ȯ
		if( IsEmpty() ) 
			error("Error: ���� ���� ���� Pop()\n");
		return m_data[m_top--];
	}

	int Peek ( ){		// �������� �ʰ� ��� ��ȯ
		if( IsEmpty() ) 
			printf("Error: ���� ���� ���� Peek()\n");
		return m_data[m_top];
	}

	// �߰����� ��� �Լ�
	void Display ( ) {		// ���� ������ ȭ�鿡 ���
		printf("[���� �׸��� �� = %2d] ==> ", m_top+1) ;
		for (int i=0 ; i<=m_top ; i++ )
			printf("%c ", m_data[i]);
		printf("\n");
	}

};

