# ZDI-22-1151: (0Day) (Pwn2Own) Oracle VirtualBox SLIRP sosendoob Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1151
- **ZDI-CAN:** ZDI-CAN-17431
- **Date:** 2022-08-23
- **CVE:** CVE-2022-39423
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Billy Jheng Bing-Jhong (@st424204), Muhammad Alifa Ramdhan (@n0psledbyte), Nguyen Hoang Thạch (@hi_im_d4rkn3ss) of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1151/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the sosendoob method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the hypervisor.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI Pwn2Own 90-day timeline. 05/18/22 – ZDI reported the vulnerability to the vendor. 08/15/22 – The vendor inquired about the vulnerability report. 08/16/22 – ZDI re-disclosed the vulnerability to the vendor. 08/16/22 – ZDI notified the vendor of the intention to publish the case as a zero-day advisory on 08/23/22. 08/16/22 – The vendor requested an extension until 10/23/22. 08/16/22 – ZDI declined the extension request. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application. The vendor fixed the issue on 18 October 2022 https://www.oracle.com/security-alerts/cpuoct2022.html

## Disclosure Timeline

- 2022-05-26 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
- 2022-10-21 - Advisory Updated
