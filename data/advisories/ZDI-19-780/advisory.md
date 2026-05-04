# ZDI-19-780: (0Day) Google Android v4l2 Double Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-780
- **ZDI-CAN:** ZDI-CAN-8316
- **Date:** 2019-09-04
- **CVE:** CVE-2019-10565
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Android
- **Credit:** Lance Jiang and Moony Li of TrendMicro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-780/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Google Android. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the v4l2 driver. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this to escalate privileges in the context of the kernel.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 03/13/19 - ZDI reported a vulnerability to the vendor 03/13/19 - The vendor acknowledged and requested further information 03/25/19 - ZDI provided the requested details 06/28/19 - The vendor confirmed the vulnerability would be fixed, but did not provide an estimated time frame 07/12/19 - ZDI requested an estimated date for the fix 07/12/19 - The vendor indicated they could not specify a date 08/21/19 - ZDI requested an update 08/26/19 - The vendor indicated there were no further updates 08/28/19 - ZDI notified the vendor of the intention to disclose the report as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it.

## Disclosure Timeline

- 2019-03-12 - Vulnerability reported to vendor
- 2019-09-04 - Coordinated public release of advisory
- 2020-03-13 - Advisory Updated
