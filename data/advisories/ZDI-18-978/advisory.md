# ZDI-18-978: Cisco WebEx Recorder and Player ATDL2006 Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-978
- **ZDI-CAN:** ZDI-CAN-5972
- **Date:** 2018-08-31
- **CVE:** CVE-2018-0379
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** b0nd @garage4hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-978/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Recorder and Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ATDL2006.DLL library. Crafted data in a WRF file can can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180718-webex-rce

## Disclosure Timeline

- 2018-05-16 - Vulnerability reported to vendor
- 2018-08-31 - Coordinated public release of advisory
- 2018-08-31 - Advisory Updated
