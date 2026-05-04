# ZDI-21-1555: Microsoft Azure Defender for IoT sync Endpoint SQL Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1555
- **ZDI-CAN:** ZDI-CAN-14159
- **Date:** 2021-12-21
- **CVE:** CVE-2021-42313
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure Defender for IoT
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1555/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Microsoft Azure Defender for IoT. Authentication is not required to exploit this vulnerability. The specific flaw exists within the sync endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to bypass authentication on the system and execute arbitrary code in the context of root.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42313

## Disclosure Timeline

- 2021-09-17 - Vulnerability reported to vendor
- 2021-12-21 - Coordinated public release of advisory
