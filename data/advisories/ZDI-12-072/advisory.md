# ZDI-12-072: Samba ReportEventW Heap Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-072
- **ZDI-CAN:** ZDI-CAN-1530
- **Date:** 2012-04-18
- **CVE:** CVE-2012-1182
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Samba
- **Affected Products:** 3.6.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-072/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samba. Authentication is not required to exploit this vulnerability. The specific flaw exists within the way Samba handles ReportEventW requests. When parsing the data send in the request Samba uses the field 'strings' to create a heap allocation but then uses another field, 'num_of_strings', to write data to the allocation. Because there is no check to see if 'num_of_strings' is smaller than 'strings' this could result in a heap buffer overflow that could lead to remote code execution.

## Additional Details

Samba has issued an update to correct this vulnerability. More details can be found at: http://www.samba.org/samba/security/CVE-2012-1182

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2012-04-18 - Coordinated public release of advisory
