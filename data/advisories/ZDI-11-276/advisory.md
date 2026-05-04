# ZDI-11-276: Adobe Flash Player MP4 sequenceParameterSetNALUnit Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-276
- **ZDI-CAN:** ZDI-CAN-975
- **Date:** 2011-08-23
- **CVE:** CVE-2011-2140
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-276/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the sequenceParameterSetNALUnit component. When handling the num_ref_frames_in_pic_order_cnt_cycle value the size is not validated and the process blindly copies user supplied data from offset_for_ref_frame into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-21.html

## Disclosure Timeline

- 2011-02-10 - Vulnerability reported to vendor
- 2011-08-23 - Coordinated public release of advisory
