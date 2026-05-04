# ZDI-26-053: Progress Software Kemp LoadMaster listapikeys Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-053
- **ZDI-CAN:** ZDI-CAN-27591
- **Date:** 2026-02-02
- **CVE:** CVE-2025-13447
- **CVSS:** 6.4
- **CVSS Vector:** AV:A/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Progress Software
- **Affected Products:** Kemp LoadMaster
- **Credit:** Alex Williams from Converge Technology Solutions
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-053/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Progress Software Kemp LoadMaster. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of user data passed to the listapikeys command. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the bal user.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://docs.progress.com/bundle/release-notes_loadmaster-7-2-62-2/page/Security-Updates.html

## Disclosure Timeline

- 2025-10-29 - Vulnerability reported to vendor
- 2026-02-02 - Coordinated public release of advisory
- 2026-02-02 - Advisory Updated
