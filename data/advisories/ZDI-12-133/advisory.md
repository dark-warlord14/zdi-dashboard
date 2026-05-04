# ZDI-12-133: GE Proficy Historian ihDataArchiver.exe Multiple Opcode Parsing Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-12-133
- **ZDI-CAN:** ZDI-CAN-1377
- **Date:** 2012-08-03
- **CVE:** CVE-2012-0229
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** GE
- **Affected Products:** Proficy Historian ihDataArchiver
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-133/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of GE iFix. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ihDataArchiver.exe process which listens by default on TCP port 14000. Several errors are present in the code responsible for parsing data from the network. By providing malformed data for opcodes 6, 7, 8, 10, and 12 the process can be made to corrupt memory which can lead to arbitrary code execution in the context of the user running the service.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: http://support.ge-ip.com/support/index?page=kbchannel&id=S:KB14767

## Disclosure Timeline

- 2011-10-17 - Vulnerability reported to vendor
- 2012-08-03 - Coordinated public release of advisory
