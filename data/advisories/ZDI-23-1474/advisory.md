# ZDI-23-1474: (0Day) Avast Premium Security Sandbox Protection Incorrect Authorization Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1474
- **ZDI-CAN:** ZDI-CAN-20178
- **Date:** 2023-09-27
- **CVE:** CVE-2023-42124
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Avast
- **Affected Products:** Premium Security
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1474/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Avast Premium Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of the sandbox feature. The issue results from incorrect authorization. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code outside the sandbox at medium integrity.

## Additional Details

02/22/23 – ZDI reported the vulnerability to the vendor. 03/03/23 – Vendor states that a fix has been prepared, and it should be included in the next release. 08/18/23 – ZDI asked for an update. 09/22/23 – ZDI asked for an update and informed the vendor that we intend to publish the case as a zero-day advisory on 09/27/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-09-27 - Coordinated public release of advisory
- 2023-10-23 - Advisory Updated
