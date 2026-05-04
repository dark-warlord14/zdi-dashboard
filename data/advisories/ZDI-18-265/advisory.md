# ZDI-18-265: Slack Technologies Slack URI Parsing Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-265
- **ZDI-CAN:** ZDI-CAN-5523
- **Date:** 2018-03-28
- **CVE:** CVE-2018-1000006
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Slack Technologies
- **Affected Products:** Slack
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-265/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Slack Technologies Slack. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of URI handlers. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Slack Technologies has issued an update to correct this vulnerability. More details can be found at: https://electronjs.org/blog/protocol-handler-fix

## Disclosure Timeline

- 2018-01-31 - Vulnerability reported to vendor
- 2018-03-28 - Coordinated public release of advisory
- 2018-04-26 - Advisory Updated
