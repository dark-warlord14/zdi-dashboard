# ZDI-21-1233: (0Day) Microsoft Windows Update Assistant Directory Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1233
- **ZDI-CAN:** ZDI-CAN-13658
- **Date:** 2021-10-27
- **CVE:** CVE-2021-43211
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1233/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within Windows Update Assistant. By creating a directory junction, an attacker can abuse Windows Update Assistant to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of Administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 06/04/21 - ZDI reported the vulnerabilities to the vendor 06/04/21 - The vendor confirmed receipt of the report 06/09/21 - The vendor requested technical clarification 06/14/21 - ZDI provided additional evidence 06/15/21 - The vendor requested technical clarification 06/18/21 - ZDI provided additional evidence 10/14/21 - The vendor communicated that the issue will not be fixed before 11/16/21 10/19/21 - ZDI notified the vendor of the intention to publish the report as 0-day advisory on 10/27/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-06-04 - Vulnerability reported to vendor
- 2021-10-27 - Coordinated public release of advisory
