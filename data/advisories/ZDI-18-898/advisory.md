# ZDI-18-898: ABB Panel Builder Animatics_SmartMotor UserSettings Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-898
- **ZDI-CAN:** ZDI-CAN-6144
- **Date:** 2018-08-10
- **CVE:** CVE-2018-10616
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ABB
- **Affected Products:** Panel Builder 800
- **Credit:** Michael DePlante - Leahy Center for Digital Investigation at Champlain College
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-898/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ABB Panel Builder 800. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the UserSettings parameter provided to the Animatics SmartMotor OPC Driver. The issue results from the lack of proper validation of a user-supplied string before using it as a format specifier. An attacker can leverage this vulnerability to execute code under the context of an administrator.

## Additional Details

ABB has issued an update to correct this vulnerability. More details can be found at: https://library.e.abb.com/public/30b77e0dc904475295401b66ec74cd3c/3BSE092089_A_en_SECURITY_-_Panel_Builder_800_Improper_input_validation_vulnerability.pdf?x-sign=OyK2T7i661JL8oQxBk+0/iWUV+hinpu8Nt6nvVmhw581vp4nkzkQbe1JSiJQPtp0

## Disclosure Timeline

- 2018-05-09 - Vulnerability reported to vendor
- 2018-08-10 - Coordinated public release of advisory
- 2018-08-10 - Advisory Updated
