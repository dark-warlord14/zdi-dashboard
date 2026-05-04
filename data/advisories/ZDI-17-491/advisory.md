# ZDI-17-491: EMC VMAX3 VASA Provider UploadConfigurator Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-491
- **ZDI-CAN:** ZDI-CAN-4641
- **Date:** 2017-07-19
- **CVE:** CVE-2017-4997
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** VMAX3 VASA Provider
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-491/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on vulnerable installations of EMC VMAX3 VASA Provider. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UploadConfigurator servlet, which listens on TCP port 5480 by default. The issue results from the web service serving files that have been uploaded by a user. An attacker can leverage this vulnerability to execute arbitrary code under the context of root.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/540783/30/0/threaded

## Disclosure Timeline

- 2017-04-05 - Vulnerability reported to vendor
- 2017-07-19 - Coordinated public release of advisory
