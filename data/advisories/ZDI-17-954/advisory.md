# ZDI-17-954: Netgain Systems Enterprise Manager script_test Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-954
- **ZDI-CAN:** ZDI-CAN-5080
- **Date:** 2017-12-13
- **CVE:** CVE-2017-17407
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-954/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of NetGain Systems Enterprise Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the content parameter provided to the script_test.jsp endpoint. A crafted content request parameter can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code under the context of the web service.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-08-04 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
