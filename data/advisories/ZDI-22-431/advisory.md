# ZDI-22-431: Kaspersky Total Security Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-431
- **ZDI-CAN:** ZDI-CAN-14233
- **Date:** 2022-03-03
- **CVE:** CVE-2021-35053
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Kaspersky
- **Affected Products:** Total Security
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-431/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Kaspersky Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Safe Browser. By creating a symbolic link, an attacker can abuse the service to overwrite a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Kaspersky has issued an update to correct this vulnerability. More details can be found at: https://support.kaspersky.com/general/vulnerability.aspx?el=12430#01112021

## Disclosure Timeline

- 2021-08-13 - Vulnerability reported to vendor
- 2022-03-03 - Coordinated public release of advisory
- 2022-03-04 - Advisory Updated
