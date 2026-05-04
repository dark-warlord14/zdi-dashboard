# ZDI-25-605: Cisco Identity Services Engine IpAccessFilter Direct Request Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-605
- **ZDI-CAN:** ZDI-CAN-26480
- **Date:** 2025-07-17
- **CVE:** CVE-2025-20285
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Identity Services Engine
- **Credit:** Kentaro Kawane of GMO Cybersecurity by Ierae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-605/
## Vulnerability Details

This vulnerability allows remote attackers to bypass IP restrictions on affected installations of Cisco Identity Services Engine. Authentication is required to exploit this vulnerability. The specific flaw exists within the configuration of the web.xml file. The issue results from an incomplete Spring Boot filter mapping. An attacker can leverage this vulnerability to bypass IP restrictions on the system.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-3VpsXOxO

## Disclosure Timeline

- 2025-05-06 - Vulnerability reported to vendor
- 2025-07-17 - Coordinated public release of advisory
- 2025-07-17 - Advisory Updated
