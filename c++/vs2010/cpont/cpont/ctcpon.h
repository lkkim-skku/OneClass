#ifdef __cplusplus
extern "C" {
#endif
	/**
	\brief �н��� cpon�� �ʱ�ȭ�մϴ�.
	\details
	\param modelpath �н��� ���� ���Ϸ� �����մϴ�. �� �������� �νĿ� cpon�� �����ϴ� ���� ���˴ϴ�.
	�ٽ� �����ڸ�, �νĿ� cpon�� �� �� ������ �о �Ű���� �����մϴ�.

	\author Leesuk Kim, lktime@skku.edu
	*/
	struct tcpnet* tcpon_initialize();

	/**
	\brief �н��⿡�� �ۼ��� model�� ��θ� �����մϴ�.
	\details
	�н��⿡�� �ۼ��� "cponmodel.csv"�� ��θ� �����մϴ�. �⺻���� "cpon/cponmodel.csv"�Դϴ�.

	\author Leesuk Kim, lktime@skku.edu
	*/
	void tcpon_setmodelpath(char* modelpath);
	
	/**
	\brief �ν��մϴ�.
	\details �Ķ���ͷ� ���� �����͸� ���� �ν��մϴ�.

	\author Leesuk Kim, lktime@skku.edu
	*/
	void tcpon_test(double* result, double* fwoutput);
	
	/**
	\brief cpon�� �Ҵ�� �޸𸮸� �����մϴ�.
	\details cpon�� �Ҵ�� �޸𸮸� �����մϴ�.

	\author Leesuk Kim, lktime@skku.edu
	*/
	void tcpon_release();

#ifdef __cplusplus
}
#endif