# ZDI-07-072: Novell NetMail AntiVirus Agent Multiple Heap Overflow Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-07-072
- **ZDI-CAN:** ZDI-CAN-162
- **Date:** 2007-12-10
- **CVE:** CVE-2007-6302
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** NetMail
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-072/
## Vulnerability Details

These vulnerabilities allow attackers to execute arbitrary code on vulnerable installations of Novell NetMail. User interaction is not required to exploit this vulnerability. The specific flaws exist in the AntiVirus agent which listens on a random high TCP port. The avirus.exe service protocol reads a user-supplied ASCII integer value as an argument to a memory allocation routine. The specified size is added to without any integer overflow checks and can therefore result in an under allocation. A subsequent memory copy operation can then corrupt the heap and eventually result in arbitrary code execution.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://secure-support.novell.com/KanisaPlatform/Publishing/990/3639135_f.SAL_Public.html

## Disclosure Timeline

- 2007-02-16 - Vulnerability reported to vendor
- 2007-12-10 - Coordinated public release of advisory
