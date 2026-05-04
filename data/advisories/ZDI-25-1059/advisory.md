# ZDI-25-1059: Vim for Windows Uncontrolled Search Path Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1059
- **ZDI-CAN:** ZDI-CAN-28569
- **Date:** 2025-12-10
- **CVE:** CVE-2025-66476
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Vim
- **Affected Products:** Vim
- **Credit:** Simon Zuckerbraun of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1059/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Vim for Windows. User interaction is required to exploit this vulnerability in that the target must open a malicious file and perform one of a set of specific actions in the editor. The specific flaw exists within the launching of external executables from the editor process. The product executes a program from an unsecured location. An attacker can leverage this vulnerability to execute code in the context of current user.

## Additional Details

Vim has issued an update to correct this vulnerability. More details can be found at: https://github.com/vim/vim/security/advisories/GHSA-g77q-xrww-p834

## Disclosure Timeline

- 2025-11-19 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
