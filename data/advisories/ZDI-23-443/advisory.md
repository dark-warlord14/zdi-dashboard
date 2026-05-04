# ZDI-23-443: Schneider Electric APC Easy UPS Online SocketService Missing Authentication Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-443
- **ZDI-CAN:** ZDI-CAN-19268
- **Date:** 2023-04-14
- **CVE:** CVE-2023-29413
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** APC Easy UPS Online
- **Credit:** Esjayy (@esj4y)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-443/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Schneider Electric APC Easy UPS Online. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SocketService module, which listens on UDP port 41222 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2023-101-04&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2023-101-04.pdf

## Disclosure Timeline

- 2022-11-30 - Vulnerability reported to vendor
- 2023-04-14 - Coordinated public release of advisory
