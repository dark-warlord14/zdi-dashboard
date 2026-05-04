# ZDI-18-552: Google Web Designer URI Parsing Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-552
- **ZDI-CAN:** ZDI-CAN-5522
- **Date:** 2018-06-06
- **CVE:** CVE-2018-1000006
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Web Designer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-552/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Web Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of URI handlers. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://electronjs.org/blog/protocol-handler-fix.

## Disclosure Timeline

- 2018-01-24 - Vulnerability reported to vendor
- 2018-06-06 - Coordinated public release of advisory
- 2018-06-06 - Advisory Updated
