# ZDI-10-230: Novell ZENworks Handheld Management ZfHIPCND.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-230
- **ZDI-CAN:** ZDI-CAN-709
- **Date:** 2010-11-07
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-230/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENworks Handheld Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within module ZfHIPCND.exe. This process is responsible for handling the data received on TCP port 2400. The module reads in the data stream and copies the specified amount of bytes into a fixed-length buffer located in the heap. An attacker can overflow this buffer and execute arbitrary code with SYSTEM privileges.

## Additional Details

TID 7007135: http://www.novell.com/support/viewContent.do?externalId=7007135&sliceId=1 Patch link, located in the TID: http://download.novell.com/Download?buildid=Sln2Lkqslmk~

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2010-11-07 - Coordinated public release of advisory
