# ZDI-22-541: (0Day) Array Networks MotionPro Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-541
- **ZDI-CAN:** ZDI-CAN-14468
- **Date:** 2022-04-04
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Array Networks
- **Affected Products:** MotionPro
- **Credit:** 3kyo0 and Jesse Chang
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-541/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Array Networks MotionPro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of URI paths. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/18/21 – ZDI reported the vulnerability to vendor 02/22/22 – ZDI requested an update 03/16/22 – The vendor advised that the issue has not been fixed 03/16/22 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 03/24/22 -- Mitigation: Array Networks has issued an update to correct this vulnerability on 03/25/22. More details can be found at: https://support.arraynetworks.net/prx/001/http/supportportal.arraynetworks.net/downloads/motionpro/MacOS/ID117847/MotionProSetup_mac.dmg

## Disclosure Timeline

- 2021-08-18 - Vulnerability reported to vendor
- 2022-04-04 - Coordinated public release of advisory
- 2022-04-04 - Advisory Updated
