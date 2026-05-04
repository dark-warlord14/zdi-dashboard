# ZDI-14-039: IBM SPSS SamplePower vsflex8l ActiveX Control ComboList Property Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-039
- **ZDI-CAN:** ZDI-CAN-1950
- **Date:** 2014-04-03
- **CVE:** CVE-2013-6724
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** SPSS
- **Credit:** Bluesea
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM SPSS SamplePower. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the IBM SPSS SamplePower VSFlexGrid8.VSFlexGridL ActiveX control. The control performs insufficient bounds checking on user-supplied data passed into the ComboList or ColComboList methods before copying it to a fixed-length buffer in global memory. An attacker can exploit this condition to achieve code execution under the context of the browser process.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21663250

## Disclosure Timeline

- 2014-01-05 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
