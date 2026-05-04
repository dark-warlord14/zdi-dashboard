# ZDI-24-449: (0Day) D-Link D-View queryDeviceCustomMonitorResult Exposed Dangerous Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-449
- **ZDI-CAN:** ZDI-CAN-21842
- **Date:** 2024-05-24
- **CVE:** CVE-2024-5298
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** D-View
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-449/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of D-Link D-View. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the queryDeviceCustomMonitorResult method. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

08/24/23 – ZDI reported the vulnerabilities to the vendor 08/24/23 – The vendor communicated that the cases would be fixed in Q4, 2023 release 05/01/24 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 05/14/24 -- Mitigation: On May 14, 2024, the vendor informed ZDI about the software update v2.0.3.88 https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10386

## Disclosure Timeline

- 2023-08-24 - Vulnerability reported to vendor
- 2024-05-24 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
