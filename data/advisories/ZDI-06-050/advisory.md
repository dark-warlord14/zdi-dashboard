# ZDI-06-050: Symantec Veritas NetBackup CONNECT_OPTIONS Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-050
- **ZDI-CAN:** ZDI-CAN-071
- **Date:** 2006-12-13
- **CVE:** CVE-2006-5822
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec
- **Affected Products:** Veritas NetBackup
- **Credit:** Sebastian Apelt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-050/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Symantec Veritas NetBackup. Authentication is not required to exploit this vulnerability. The specific flaw exists within bpcd.exe during the parsing of overly long CONNECT_OPTIONS requests to a NetBackup Master/Media Server. When the CONNECT_OPTIONS command is parsed, the contents are copied into a stack allocated buffer without proper length checking. Exploitation of this vulnerability can lead to complete system compromise.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/avcenter/security/Content/2006.12.13a.html

## Disclosure Timeline

- 2006-08-14 - Vulnerability reported to vendor
- 2006-12-13 - Coordinated public release of advisory
