# ZDI-21-1595: Microsoft Azure Defender for IoT maintenanceWindow Endpoint SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1595
- **ZDI-CAN:** ZDI-CAN-14189
- **Date:** 2021-12-23
- **CVE:** CVE-2021-41365
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure Defender for IoT
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1595/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Microsoft Azure Defender for IoT. Authentication is required to exploit this vulnerability. The specific flaw exists within the maintenanceWindow endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41365

## Disclosure Timeline

- 2021-09-16 - Vulnerability reported to vendor
- 2021-12-23 - Coordinated public release of advisory
