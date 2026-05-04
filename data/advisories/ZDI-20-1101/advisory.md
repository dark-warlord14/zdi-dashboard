# ZDI-20-1101: Cisco RV340 upload.cgi Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1101
- **ZDI-CAN:** ZDI-CAN-10907
- **Date:** 2020-09-08
- **CVE:** CVE-2020-3453
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** 0x00string
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1101/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV340 routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the fileparam parameter provided to the upload.cgi endpoint. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-rv-osinj-rce-pwTkPCJv

## Disclosure Timeline

- 2020-06-02 - Vulnerability reported to vendor
- 2020-09-08 - Coordinated public release of advisory
