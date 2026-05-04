# ZDI-06-049: Symantec Veritas NetBackup Long Request Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-049
- **ZDI-CAN:** ZDI-CAN-070
- **Date:** 2006-12-13
- **CVE:** CVE-2006-6222
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec
- **Affected Products:** Veritas NetBackup
- **Credit:** Sebastian Apelt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-049/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Symantec Veritas NetBackup. Authentication is not required to exploit this vulnerability. The specific flaw exists within bpcd.exe during the parsing of overly long requests to a NetBackup Master/Media Server. Communications to this process are prefixed with a length, which, if malformed can result in a stack based buffer overflow. Exploitation of this vulnerability can lead to complete system compromise.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/avcenter/security/Content/2006.12.13a.html

## Disclosure Timeline

- 2006-08-14 - Vulnerability reported to vendor
- 2006-12-13 - Coordinated public release of advisory
