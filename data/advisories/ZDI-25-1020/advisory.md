# ZDI-25-1020: Arista NG Firewall runTroubleshooting Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1020
- **ZDI-CAN:** ZDI-CAN-27310
- **Date:** 2025-11-25
- **CVE:** CVE-2025-6978
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Arista
- **Affected Products:** NG Firewall
- **Credit:** Gereon Huppertz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1020/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Arista NG Firewall. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the implementation of the runTroubleshooting method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Arista has issued an update to correct this vulnerability. More details can be found at: https://www.arista.com/en/support/advisories-notices/security-advisory/22535-security-advisory-0123

## Disclosure Timeline

- 2025-06-18 - Vulnerability reported to vendor
- 2025-11-25 - Coordinated public release of advisory
- 2025-11-25 - Advisory Updated
