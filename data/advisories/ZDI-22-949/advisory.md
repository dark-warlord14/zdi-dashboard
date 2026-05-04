# ZDI-22-949: (0Day) xhyve e1000 Stack-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-949
- **ZDI-CAN:** ZDI-CAN-15056
- **Date:** 2022-07-06
- **CVE:** CVE-2022-35867
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** xhyve
- **Affected Products:** xhyve
- **Credit:** Alisa Esage of Zero Day Engineering (zerodayengineering.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-949/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of xhyve. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the e1000 virtual device. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120-day deadline. 10/21/21 – ZDI attempted to contact the vendor and obtain secure keys. 10/22/21 – The contact advised they were only a one-time contributor but provided their key and agreed to receive the notification in case this was about their contribution. 10/22/21 – The contact provided a GitHub link pointing to the admin of the repository as well as their contact information. 10/25/21 – The project owner advises to send the information, but also notes that the problem could have originated in FreeBSD’s bhyve. This issue was fixed in FreeBSD’s bhyve under CVE-2019-5609 and the code was never updated in xhyve. 10/25/21 – ZDI re-notified the case to the project owner and advised him to review the potential to notify FreeBSD. 06/24/22 – ZDI verified that this code was still vulnerable as of this date. 06/29/22 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 07/6/22 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-10-22 - Vulnerability reported to vendor
- 2022-07-06 - Coordinated public release of advisory
- 2022-07-14 - Advisory Updated
