# ZDI-24-574: Trend Micro InterScan Web Security Virtual Appliance Cross-Site Scripting Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-574
- **ZDI-CAN:** ZDI-CAN-21495
- **Date:** 2024-06-06
- **CVE:** CVE-2024-36359
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-574/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Trend Micro InterScan Web Security Virtual Appliance. Authentication is required to exploit this vulnerability. The specific flaw exists within the HTTP Inspection component. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000298065

## Disclosure Timeline

- 2023-09-05 - Vulnerability reported to vendor
- 2024-06-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
