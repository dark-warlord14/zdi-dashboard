# ZDI-24-785: PaperCut MF EmailRenderer Server-Side Template Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-785
- **ZDI-CAN:** ZDI-CAN-23481
- **Date:** 2024-06-18
- **CVE:** CVE-2024-1882
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** PaperCut
- **Affected Products:** MF
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-785/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of PaperCut MF. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the EmailRenderer class. The issue results from the lack of proper validation of a user-supplied string before processing it with the template engine. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

PaperCut has issued an update to correct this vulnerability. More details can be found at: https://www.papercut.com/kb/Main/Security-Bulletin-March-2024

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
