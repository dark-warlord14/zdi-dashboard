# ZDI-25-607: Cisco Identity Services Engine enableStrongSwanTunnel Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-607
- **ZDI-CAN:** ZDI-CAN-26481
- **Date:** 2025-07-17
- **CVE:** CVE-2025-20337
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Identity Services Engine
- **Credit:** Kentaro Kawane of GMO Cybersecurity by Ierae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-607/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco Identity Services Engine. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the enableStrongSwanTunnel method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the iseadminportal user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-unauth-rce-ZAd2GnJ6

## Disclosure Timeline

- 2025-05-06 - Vulnerability reported to vendor
- 2025-07-17 - Coordinated public release of advisory
- 2025-07-17 - Advisory Updated
