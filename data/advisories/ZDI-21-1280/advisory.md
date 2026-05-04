# ZDI-21-1280: Kaspersky Total Security Directory Traversal Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1280
- **ZDI-CAN:** ZDI-CAN-14234
- **Date:** 2021-11-09
- **CVE:** CVE-2021-35053
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Kaspersky
- **Affected Products:** Total Security
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1280/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Kaspersky Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within Kaspersky Lab Launcher. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Kaspersky has issued an update to correct this vulnerability. More details can be found at: https://support.kaspersky.com/general/vulnerability.aspx?el=12430#01112021

## Disclosure Timeline

- 2021-08-25 - Vulnerability reported to vendor
- 2021-11-09 - Coordinated public release of advisory
