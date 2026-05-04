# ZDI-21-1273: (0Day) Bitdefender Total Security Unnecessary Privileges Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1273
- **ZDI-CAN:** ZDI-CAN-13950
- **Date:** 2021-10-28
- **CVE:** CVE-2021-3579 , CVE-2021-3576
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bitdefender
- **Affected Products:** Total Security
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1273/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Bitdefender Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the endpoint client. The issue results from allowing an untrusted process to impersonate the client of a pipe. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/21/21 - ZDI reported the vulnerabilities to the vendor 05/21/21 - The vendor confirmed receipt of the reports 05/27/21 - The vendor communicated that they were working on a fix 06/04/21 - The vendor provided the CVEs and requested technical clarification 06/06/21 - ZDI provided additional evidence 10/20/21 - ZDI requested an update 10/20/21 - The vendor advised that the vulnerabilities affect a third-party component and requested for an extension until 11/12/21 10/21/21 - ZDI notified the vendor of the intention to publish these reports as 0-day advisories on 10/28/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-05-27 - Vulnerability reported to vendor
- 2021-10-28 - Coordinated public release of advisory
