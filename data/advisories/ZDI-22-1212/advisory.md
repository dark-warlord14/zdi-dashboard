# ZDI-22-1212: (0Day) NIKON NIS-Elements Viewer ND2 File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1212
- **ZDI-CAN:** ZDI-CAN-15072
- **Date:** 2022-09-14
- **CVE:** CVE-2022-40656
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NIKON
- **Affected Products:** NIS-Elements Viewer
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1212/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NIKON NIS-Elements Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ND2 files. Crafted data in a ND2 file can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

09/24/21 – ZDI reported the vulnerabilities to the vendor. 02/24/22 – ZDI requested an update. 03/02/22 – ZDI requested an update. 03/29/22 – The vendor asked for the reports to be sent again. 03/29/22 – ZDI resent the reports to the vendor. 08/24/22 – ZDI requested an update. 08/24/22 – The vendor advised that the reports did not meet the bar for servicing because it is a legacy product. 09/09/22 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories on 09/13/22. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-03-29 - Vulnerability reported to vendor
- 2022-09-14 - Coordinated public release of advisory
