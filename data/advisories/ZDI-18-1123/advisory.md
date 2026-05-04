# ZDI-18-1123: Cisco Webex Recorder and Player ATAS32 Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1123
- **ZDI-CAN:** ZDI-CAN-6317
- **Date:** 2018-10-08
- **CVE:** CVE-2018-15416
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Michael Flanders of the Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1123/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of WRF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute arbitrary code in the context of an administrator.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20181003-webex-rce

## Disclosure Timeline

- 2018-06-08 - Vulnerability reported to vendor
- 2018-10-08 - Coordinated public release of advisory
- 2018-10-08 - Advisory Updated
