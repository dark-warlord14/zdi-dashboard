# ZDI-18-882: ABB Panel Builder Begalil IPAddress Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-882
- **ZDI-CAN:** ZDI-CAN-5786
- **Date:** 2018-08-10
- **CVE:** CVE-2018-10616
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ABB
- **Affected Products:** Panel Builder 800
- **Credit:** Michael DePlante - Leahy Center for Digital Investigation at Champlain College
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-882/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ABB Panel Builder 800. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the IPAddress parameter of the ABB Galil DMC Series OPC Driver. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of an administrator.

## Additional Details

ABB has issued an update to correct this vulnerability. More details can be found at: https://library.e.abb.com/public/30b77e0dc904475295401b66ec74cd3c/3BSE092089_A_en_SECURITY_-_Panel_Builder_800_Improper_input_validation_vulnerability.pdf?x-sign=OyK2T7i661JL8oQxBk+0/iWUV+hinpu8Nt6nvVmhw581vp4nkzkQbe1JSiJQPtp0

## Disclosure Timeline

- 2018-04-04 - Vulnerability reported to vendor
- 2018-08-10 - Coordinated public release of advisory
- 2018-08-10 - Advisory Updated
