# ZDI-14-360: Hewlett-Packard Sprinter TTF16.ocx CopyRange/CopyRangeEx Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-360
- **ZDI-CAN:** ZDI-CAN-2342
- **Date:** 2014-10-14
- **CVE:** CVE-2014-2637
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Sprinter
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-360/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Sprinter. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability is found in Tidestone Formula One ActiveX controls, which are installed as a part of HP Sprinter. By providing improper parameters to the methods CopyRange or CopyRangeEx provided by those controls, an attacker can execute code in the context of the browser.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04454636

## Disclosure Timeline

- 2014-05-30 - Vulnerability reported to vendor
- 2014-10-14 - Coordinated public release of advisory
