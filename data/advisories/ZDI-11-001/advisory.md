# ZDI-11-001: Microsoft Data Access Components DSN Overflow Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-001
- **ZDI-CAN:** ZDI-CAN-708
- **Date:** 2011-01-11
- **CVE:** CVE-2011-0026
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Data Access Components
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-001/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Data Access Components. The vulnerability is present in an API call and as such successful exploitation will depend on an application's implementation of this call. The specific flaw exists within the SQLConnectW call in the odbc32.dll component. When calculating the size of a user provided szDSN, the result of a call to lstrlenW is used in a signed comparison to SQL_MAX_DSN_LENGTH to verify the destination buffer size. This value is later used to copy user supplied data to a fixed length stack buffer. A malicious szDSN length could be used to exploit this signedness bug and execute arbitrary code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS11-002.mspx

## Disclosure Timeline

- 2010-06-23 - Vulnerability reported to vendor
- 2011-01-11 - Coordinated public release of advisory
