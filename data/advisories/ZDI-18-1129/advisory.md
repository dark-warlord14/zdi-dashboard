# ZDI-18-1129: Cisco WebEx Recorder and Player ATAS32 Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1129
- **ZDI-CAN:** ZDI-CAN-6801
- **Date:** 2018-10-08
- **CVE:** CVE-2018-15413
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Michael Flanders of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1129/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Recorder and Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of WRF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20181003-webex-rce

## Disclosure Timeline

- 2018-07-25 - Vulnerability reported to vendor
- 2018-10-08 - Coordinated public release of advisory
- 2018-10-08 - Advisory Updated
