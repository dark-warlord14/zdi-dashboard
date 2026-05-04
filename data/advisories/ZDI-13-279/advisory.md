# ZDI-13-279: EMC Connectrix Manager Converged Network Edition FileUploadController Servlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-279
- **ZDI-CAN:** ZDI-CAN-1746
- **Date:** 2013-12-18
- **CVE:** CVE-2013-6810
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** Connectrix Manager Converged Network Edition
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-279/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC Connectrix Manager Converged Network Edition. Authentication is not required to exploit this vulnerability. The specific flaw exists within the 'FileUploadController' servlet, which allows an unauthenticated user to upload an arbitrary file anywhere on the system. An attacker can leverage this directory traversal vulnerability into arbitrary code execution on the compromised server in the security context of the Administrator account.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://my.brocade.com/wps/myportal/!ut/p/b1/04_SjzQ0MzEwM7S0sDDSj9CPykssy0xPLMnMz0vMAfGjzOKd3BzDjE2MjQ39vbycDTzdXYJCLb18jQx8zIAKIoEKDHAARwNC-sP1o_ArMYEqwGOFn0d-bqp-blSOpaeuoyIA_fi0nA!!/dl4/d5/L2dJQSEvUUt3QS80SmtFL1o2X0JGQVYzNDMzMU9KSkMwSUdEUlU5Sk0yMDcx/

## Disclosure Timeline

- 2013-02-01 - Vulnerability reported to vendor
- 2013-12-18 - Coordinated public release of advisory
