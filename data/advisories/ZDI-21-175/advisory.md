# ZDI-21-175: McAfee Total Protection Directory Junction Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-175
- **ZDI-CAN:** ZDI-CAN-12081
- **Date:** 2021-02-10
- **CVE:** CVE-2021-23873
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** McAfee
- **Affected Products:** Total Protection
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-175/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of McAfee Total Protection. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of the QuickClean feature. By creating a directory junction, an attacker can abuse QuickClean to delete a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

McAfee has issued an update to correct this vulnerability. More details can be found at: http://service.mcafee.com/FAQDocument.aspx?&id=TS103114

## Disclosure Timeline

- 2020-11-13 - Vulnerability reported to vendor
- 2021-02-10 - Coordinated public release of advisory
