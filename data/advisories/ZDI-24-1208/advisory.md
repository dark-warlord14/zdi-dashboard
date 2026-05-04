# ZDI-24-1208: (0Day) Visteon Infotainment System DeviceManager iAP Serial Number SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1208
- **ZDI-CAN:** ZDI-CAN-20112
- **Date:** 2024-09-11
- **CVE:** CVE-2024-8355
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Visteon
- **Affected Products:** Infotainment
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1208/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of Visteon Infotainment system. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DeviceManager. When parsing the iAP Serial number, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

08/16/24 – ZDI reported the vulnerability to the vendor 08/30/24 – ZDI asked for updates 09/03/24 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory, if no response was received by 09/10/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2023-01-12 - Vulnerability reported to vendor
- 2024-09-11 - Coordinated public release of advisory
- 2024-09-11 - Advisory Updated
