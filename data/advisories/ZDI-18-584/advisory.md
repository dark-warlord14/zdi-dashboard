# ZDI-18-584: Tencent Foxmail URI parsing Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-584
- **ZDI-CAN:** ZDI-CAN-5543
- **Date:** 2018-06-13
- **CVE:** CVE-2018-11616
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Tencent
- **Affected Products:** Foxmail
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-584/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Tencent Foxmail. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of URI handlers. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Fixed in version 7.2.9

## Disclosure Timeline

- 2018-01-25 - Vulnerability reported to vendor
- 2018-06-13 - Coordinated public release of advisory
- 2018-06-13 - Advisory Updated
