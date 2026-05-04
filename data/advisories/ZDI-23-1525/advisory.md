# ZDI-23-1525: (0Day) D-Link DIR-X3260 SetSysEmailSettings SMTPServerAddress Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1525
- **ZDI-CAN:** ZDI-CAN-21222
- **Date:** 2023-10-04
- **CVE:** CVE-2023-44427
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-X3260
- **Credit:** Nicholas Zubrisky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1525/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-X3260 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within prog.cgi, which handles HNAP requests made to the lighttpd webserver listening on TCP ports 80 and 443. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

06/05/23 – ZDI reported the vulnerability to the vendor. 09/29/23 – ZDI asked for an update and informed the vendor that the case will be published as a zero-day advisory on 10/04/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-06-05 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
