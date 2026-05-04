# ZDI-20-663: (0Day) Microsoft Windows splwow64 Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-663
- **ZDI-CAN:** ZDI-CAN-9851
- **Date:** 2020-05-19
- **CVE:** CVE-2020-0986
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-663/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the user-mode printer driver host process splwow64.exe. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to escalate privileges from low integrity and execute code in the context of the current user at medium integrity.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 12/31/19 – ZDI sent the vulnerability report to the vendor and the vendor provided a case ID 02/28/20 – The report appeared on track in a monthly report 04/06/20 – The report appeared on track in a monthly report 05/07/20 – The vendor notified ZDI they would miss the 05/12/20 patch date, but did offer a beta for testing 05/08/20 – ZDI agreed to test 05/12/20 – ZDI confirmed the beta patch succeeded, but also communicated the intent to publish the reports as 0-day as extension options are expired -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it.

## Disclosure Timeline

- 2019-12-31 - Vulnerability reported to vendor
- 2020-05-19 - Coordinated public release of advisory
